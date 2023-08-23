#include <iostream>
using namespace std;
int val=0;
class RunDCode
{
    public :
    RunDCode()
    {
        cout<<++val;

    }
    ~RunDCode()
    {
        cout<<val--;
    }

};
int main()
{
    RunDCode objRun1,objRun2,objRun3;
    {
        RunDCode objRun4;
    }
    return 0;
}