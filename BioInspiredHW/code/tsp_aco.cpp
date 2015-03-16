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
	bool visit;		// if edge has been visited
};

// Function prototypes
void saco( int max_it, int ants, Edge edges[31][31] );

void saco( int max_it, int ants, Edge edges[31][31] )
{
	int tau_y = 0;
	int best[31];
	int paths[ants][31];
	int i, j, t = 0;
	int start = 0;

	while( t < max_it )
	{
		// build a solution for each ant
		for( i = 0; i < ants; i++ )
		{
			// place on random starting node
			start = rand()%32;
			best[0] = start;

			// probablastically move to next node	
			for( j = 0; j < 32; j++ )
			{
				if( j == start )

				move = 0;
			}

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
		}
	}
	
	// run simple aco
	saco( 100, 100, edges );
	
	srand( time(NULL) );
	
	return 1;
}

