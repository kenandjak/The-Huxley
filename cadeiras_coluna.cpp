#include <iostream>

int main() {
  int total,quantidade,numero;
  std::cin>>total>>quantidade>>numero;
  while(numero <= total){
    std::cout<<numero<<"\n";
    numero += quantidade;
  }  
}