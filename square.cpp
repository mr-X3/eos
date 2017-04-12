#include<stdlib.h> 
#include<signal.h> 
#include<iostream>  
#include<string>   


using namespace std;
void delay(int num);  

int main()
{
int option;
string frq;
string command;

while(1)
        {
                                                                                
cout <<  "\n1.  Press 1 to set the Beagle Board CPU Frequency\n";               
cout <<  "2.  Press 2 to get the current CPU Frequency\n";                      
cout <<  "3.  Press 3 or CNTR-Z to exit\n";                                     
cin >> option;                                                                  
                                                                                
switch(option)                                                                  
        {                                                                       
        case 1:                                                                 
                cout << "Please Enter the frequency in range 100-1000 (MHz)\n"; 
                cin >> frq;                                                     
                command="cpufreq-set -f "+frq+"MHz";                            
                                                                                
                if(system(command.c_str()))                                     
                cout << "\nCannot Set the Frequency. Make sure logged in as ROOT\n";
                                            break;                                    
                                                                                
                                                                                
        case 2:                                                                 
                                                          
                                        
                {                                                               
                        cout << "Press any key to go Back in main menu \n";         
                                                                                
                        system("cpufreq-info | tail -2");                       
                        delay(50000);                                           
                }                                                               
       		 break;                                                          
                                                                       
        case 3:                                                                 
                exit(0);                                                        
                                                                                
        }                                                                       
        }                                                                       
}                                                                               
void delay(int num)                                                             
{                                                                               
        int i,j;                                                                
        for(i=0; i < num;i++)                                                      
                for(j=0; j < 1275;j++);                                            
} 
