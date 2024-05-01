#include <bits/stdc++.h>
using namespace std;

int main(){
  int n;
  cin >> n;
  int m;
  vector<int>sequencia(n);
  for(int i = 0; i < n; i++){
    cin >> m;
    sequencia[i] = m;
  }
  int circulado = 1;
  int posicao = 0;
  while(posicao < sequencia.size() - 1){
    if(sequencia[posicao+1] != sequencia[posicao]){
      circulado += 1;
    }
    posicao += 1;
  }
  cout << circulado << "\n";
}