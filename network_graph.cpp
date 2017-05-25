#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int FlipCoin(float alpha)
{
    float modified_alpha = alpha*100;
    
    double guess = rand() % 100 + 1;
    
    if (guess < modified_alpha) { return 1; }
    else { return 0;  }
}

void CreateGraph(int nodes, string topology, float alpha, int node_min, int node_max, int link_min, int link_max)
{
    srand(time(NULL));
    
    ofstream output;
    output.open("graph_output.txt");
    
    for (int i = 0; i < nodes; i++)
    {
        int j = i + 1;
        if (topology == "linear" && j < nodes)
        {
            output << i << " " << j << " " << rand() % (link_max - link_min + 1) + link_min << endl;
        }
        
        if (topology == "full")
        {
            for (int j = i+1; j < nodes; j++)
            {
                output << i << " " << j << " " << rand() % (link_max - link_min + 1) + link_min << endl;
            }
        }

        if (topology == "random")
        {
            for (int j = i+1; j < nodes; j++)
            {
                int coin = FlipCoin(alpha);
                if (coin == 1)
                {
                    output << i << " " << j << " " << rand() % (link_max - link_min + 1) + link_min << endl;
                }
            }
        }
    }
    
    if (topology == "star")
    {
        for (int j = 1; j < nodes; j++)
        {
            output << 0 << " " << j << " " << rand() % (link_max - link_min + 1) + link_min << endl;
        }
    }
    
    for (int i = 0; i < nodes; i++)
    {
        output << rand() % (node_max - node_min + 1) + node_min << " ";
    }
    output << endl;
    
    output.close();
}

int main()
{
    
    int nodes, node_min, node_max, link_min, link_max;
    float alpha;
    string topology, filename;
    
    ifstream config;
    cout << "Enter configuration file name: " << endl;
    cin >> filename;
    config.open(filename);
    
    for (int i = 0; i < 7; i++)
    {
        if (i==0)
        {
            config >> nodes;
        }
        
        else if (i==1)
        {
            config >> topology;
        }
        
        else if (i==2)
        {
            config >> alpha;
        }
        
        else if (i==3)
        {
            config >> node_min;
        }
    
        else if (i==4)
        {
            config >> node_max;
        }
        
        else if (i==5)
        {
            config >> link_min;
        }
        else if (i==6)
        {
            config >> link_max;
        }
    }
    
    config.close();
    
    CreateGraph(nodes, topology, alpha, node_min, node_max, link_min, link_max);
    
    return 0;
    
}
