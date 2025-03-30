#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    int x = 2;
    int caule = n/2;
    for(int i=1; i<=n; i++) {
        string xis = "";
        int spaces = n;
        while(spaces-i > 0) {
            cout << " ";
            spaces--;
        }
        for(int j=1; j<=i*2; j++){
            xis += "X";
        }
        cout << xis << "\n";
    }
    for(int i=1; i<=n/2; i++) {
        int spaces = n;
        while(spaces-1 > 0) {
            cout << " ";
            spaces--;
        }
        cout << "XX" << "\n";
    }
}
//g++ -std=gnu++17 -O2 -static -o c arvore_natal.cpp