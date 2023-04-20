#include <iostream>
using namespace std;

int main() {
    int a,b,n;
    int gcd=1;
    cin>>a>>b;
    if(a>b)
    n=b;
    else 
    n=a;
    for (int i=2;i<=n;i++)
    {
        if((a%i==0)&&(b%i==0))
            gcd=i;
    }
cout<<"\n"<<gcd;
    return 0;
}
