#include <iostream>
#include<string.h>
using namespace std;



int main() {
    // Write C++ code here
    string str1,str2,str3;
    str1="prep";
    str2="bytesyt";
    str3="Pocopine";
    cout<<"First occurence of 'rep'in "<<str1<<"="<<str1.find("rep")<<endl;
    cout<<"last occurence of 'yt' in "<<str2<<"="<<str2.rfind("yt")<<endl;
    

    return 0;
}
