#include<iostream>
using namespace std;
int fact(int num);
int main()
{
int n;
cin>>n;
cout<<fact(n);
return 0;
}
int fact(int num)
{
if(num==0)
return 1;
else
return num*fact(num-1);
}
