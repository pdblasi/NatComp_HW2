// Author: Stephanie Athow
// Date: 15 March 2015
// Professor: Dr. Jeff McGough
// Program: Traveling Salesman Problem using Ant Colony Optomization

#include <iostream>
#include <fstream>
#include <cmath>
#include <ctime>
#include <cstdlib>

using namespace std;

struct Edge
{
	int city1;		
	int city2;		
	int pheromone;		// amount of pheromone
	float distance;		// distance between cities
	float visibility;	
	bool visit;			// if edge has been visited
	
};

// Function prototypes
void saco( int max_it, int ants, Edge edges[31][31] );

void saco( int max_it, int ants, Edge edges[31][31] )
{
	int tau_y = 0;
	int best[31];
	int paths[ants][31];
	int i, j, k, m, t = 0;
	int curr = 0;
	int city_traveled [31] = {0};
	int path_counter = 0;
	float alpha = 0.5;
	float beta = 0.0;
	float sum = 0.0;
	float probability = 0.0;
	float probabilities[31];

	while( t < max_it )
	{
		// build a solution for each ant
		for( i = 0; i < ants; i++ )
		{
			// place on random starting node
			curr = rand()%32;
			paths[i][0] = curr;
			path_counter++;
			city_traveled[curr] = 1;
			
			while(path_counter < 32)
			{
			
				// find sum of pheromones on remaining untraveled edges
				j = 0;
				sum = 0;
				for( j = 0; j < 32; j++ )
				{
					if( city_traveled[j] == 0 )
					{
						sum += edges[curr][j].pheromone;
					}

				}
				
				j = 0;

				// generate probability list for current node
				for( j = 0; j < 32; j++ )
				{
					if( city_traveled[j] == 0 )
					{	
						probability = ( pow(edges[curr][j].pheromone,alpha )*
							pow(edges[curr][j].visibility,beta))/
							(sum * pow(edges[curr][j].visibility, beta ) );
						probabilities[j] = probability;
					}
					else if( city_traveled[j] == 1 )
						probabilities[j] = probability;
					j++;
				}

				// create move chance
				double move = ( (double)rand()/(RAND_MAX) ) ;
				
				for( int z = 0; z < 32; z++ )
				{
					if( probabilities[z] > move )
					{
						city_traveled[j] = 1;
						paths[i][path_counter] = j;
						path_counter++;
						curr = z;
						break;
					}
				}
	 	
			}
			
			// reset all information to zero for next ant
			for( k = 0; k < 32; k++ )
				city_traveled[k] = 0;
			path_counter = 0;
			}

		//evaluate solutions
		t++;
	}

	return;
}

int main()
{
	int x, y, index = 0;		// read in city information from text file
	int i, j;			// index counters
	int cities[31] [2];		// holds city locations from file
	Edge edges[31] [31];		// holds an array of Edges (struct)
	ifstream fin ("TSP.txt");	// file to read in city information
	float xdist, ydist;		// used to calc dist between cities

	//cout << "after inits" << endl;

	// read in cities locations from file
	// NOTE: my file starts cities at 1, so it's index-1 to get correct 
	// index number
	if ( fin.is_open() )
	{
		//cout << "file open" << endl;
		while( fin >> index )
		{
			//cout << "index is: " << index << endl;
			fin >> x >> y;
			cities[index - 1][0] = x;
			cities[index - 1][1] = y;
		}
	}

	// cout << "after if" << endl;

	// Fill edges array with all correct information
	for( i = 0; i < 32-1; i++ )
	{
		for( j = i+1; j < 32; j++)
		{
			edges[i][j].city1 = i;
			edges[i][j].city2 = j;
			// calc x and y distances for distance formula
			xdist = pow( ( cities[i][0] - cities[j][0] ), 2);
			ydist = pow( ( cities[i][1] - cities[j][1] ), 2 );  
			edges[i][j].distance = sqrt( xdist + ydist );
			edges[i][j].pheromone = 1;
			edges[i][j].visit = false;
			edges[i][j].visibility = 1 / edges[i][j].distance;
		}
	}
	
	// run simple aco
	saco( 100, 32, edges );
	
	srand( time(NULL) );
	
	return 1;
}

