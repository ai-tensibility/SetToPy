#include <vector>
#include <algorithm>

struct SetElement {
    double x;
    double y;
    double value;
};

class SetTopy {
private:
    std::vector<SetElement> elements;

public:
    void add(double x, double y, double value) {
        for (const auto& element : elements) {
            if (element.x == x && element.y == y && element.value == value) {
                return;  // Element already exists
            }
        }
        elements.push_back({x, y, value});
    }

    bool contains(double x, double y, double value) {
        for (const auto& element : elements) {
            if (element.x == x && element.y == y && element.value == value) {
                return true;
            }
        }
        return false;
    }

    void remove(double x, double y, double value) {
        elements.erase(std::remove_if(elements.begin(), elements.end(),
                                      [x, y, value](const SetElement& element) {
                                          return element.x == x && element.y == y && element.value == value;
                                      }),
                       elements.end());
    }

    std::vector<SetElement> get_elements() const {
        return elements;
    }

    size_t size() const {
        return elements.size();
    }
};
