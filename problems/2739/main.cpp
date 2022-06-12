// 2739. 구구단

#include <iostream>

int main()
{
    int number = 0;

    std::cin >> number;

    for (int multiplier = 1; multiplier < 10; ++multiplier)
    {
        std::cout << number << " * " << multiplier << " = " << number * multiplier << std::endl;
    }
}
