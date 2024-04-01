#include <iostream>

int main() {
    int year;
    std::cin>>year;
    if (year % 4 != 0 or(year%100==0 and year%400!=0)){
        std::cout<<"NAOBISSEXTO";
    }else{
        std::cout<<"BISSEXTO";
  }
}