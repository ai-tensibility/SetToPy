// settopy.cpp

#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

struct SetElement {
    double x, y, value;
};

struct Node {
    int id;
    double x, y, value;
};

struct Hyperedge {
    std::unordered_set<int> node_ids;

    bool operator==(const Hyperedge& other) const {
        return node_ids == other.node_ids;
    }
};

struct HyperedgeHash {
    std::size_t operator()(const Hyperedge& e) const {
        std::size_t hash = 0;
        for (int id : e.node_ids) {
            hash ^= std::hash<int>{}(id) + 0x9e3779b9 + (hash << 6) + (hash >> 2);
        }
        return hash;
    }
};

class SetTopy {
private:
    std::unordered_map<int, Node> nodes;
    std::unordered_set<Hyperedge, HyperedgeHash> hyperedges;
    int current_id = 0;

public:
    // Public interface for simple set operations
    void add(double x, double y, double value) {
        int id = current_id++;
        nodes[id] = Node{id, x, y, value};
        add_hyperedge({id});
    }

    bool contains(double x, double y, double value) const {
        for (const auto& pair : nodes) {
            const Node& node = pair.second;
            if (node.x == x && node.y == y && node.value == value) {
                return true;
            }
        }
        return false;
    }

    void remove(double x, double y, double value) {
        for (auto it = nodes.begin(); it != nodes.end(); ++it) {
            if (it->second.x == x && it->second.y == y && it->second.value == value) {
                int id = it->first;
                nodes.erase(it);
                remove_node(id);
                return;
            }
        }
    }

    std::vector<std::tuple<double, double, double>> get_elements() const {
        std::vector<std::tuple<double, double, double>> elements;
        for (const auto& pair : nodes) {
            const Node& node = pair.second;
            elements.emplace_back(node.x, node.y, node.value);
        }
        return elements;
    }

    size_t size() const {
        return nodes.size();
    }

private:
    void add_node(int id) {
        // Hidden internal method to add a node
    }

    void add_hyperedge(const std::vector<int>& node_ids) {
        Hyperedge edge;
        for (int id : node_ids) {
            edge.node_ids.insert(id);
        }
        hyperedges.insert(edge);
    }

    void remove_node(int id) {
        for (auto it = hyperedges.begin(); it != hyperedges.end(); ) {
            if (it->node_ids.find(id) != it->node_ids.end()) {
                it = hyperedges.erase(it);
            } else {
                ++it;
            }
        }
    }
};

// Ensure this file is included in settopy_bindings.cpp
