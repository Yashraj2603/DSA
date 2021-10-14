#include <iostream>

using namespace std;
void rotate(int arr[],int n,int d)
{
    for(int i=0;i<d;i++){
    int temp=arr[0];
    for(int i=0;i<n-1;i++)
    arr[i]=arr[i+1];
    arr[n-1]=temp;
    }
    cout<<"array=";
    for(int j=0;j<n;j++)
    cout<<arr[j]<<endl;
}

int main()
{
   int n,d;
   cin>>n;
   int arr[n];
   for(int i=0;i<n;i++)
   cin>>arr[i];
   cin>>d;
   rotate(arr,n,d);
   return 0;
}
