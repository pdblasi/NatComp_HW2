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
	float pheromone;		// amount of pheromone
	float distance;		// distance between cities
	float visibility;	
	bool visit;			// if edge has been visited
	
};

// Function prototypes
float saco( int max_it, int ants, Edge edges[31][31] );
float path_eval( int paths[][31], Edge edges[31][31] );
float sum_pheromone( int curr, int city_traveled[], Edge edges[][31] );
void prob_list( int curr, int sum_p, float probabilities[31], int city_traveled[], Edge edges[][31] );


// Functions
float saco( int max_it, int ants, Edge edges[31][31] )
{
	int paths[ants][31];
	int i, j, k, m, t = 0;
	int curr = 0;
	int city_traveled [31] = {0};
	int path_counter = 0;

	float sum_p = 0.0;
	float probability = 0.0;
	float probabilities[31];
	float path_try;
	float path_best = 10000.0;

	while( t < max_it )
	{
		// build a solution for each ant
		for( i = 0; i < 1; i++ )
		{
			
			cout << "ant number: " << i << endl;

			// place on random starting node
			curr = rand()%32;
			paths[i][0] = curr;
			path_counter++;
			city_traveled[curr] = 1;
			cout << "rand curr: " << curr << endl;
			
			while(path_counter < 2)
			{
				//cout << "path count: " << path_counter << endl;
	
				// find sum of pheromones on remaining untraveled edges
				sum_p = 0;
				//sum_p = sum_pheromone( curr, city_traveled, edges );
				// array is not being filled correctly!

				//cout << "Sum pheromone: " << sum_p << endl;
				//cout << "curr: " << curr << endl;
				path_counter ++;

				//spoof sum_p for debugging other functions
				sum_p = 32 - path_counter;

				// generate probability list for current node
				prob_list( curr, sum_p, probabilities, city_traveled, edges );

				//	cout << "probability list" << endl;

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
						//cout << "moved to: " << z << endl;
						break;
					}
				}
	 		 	//cout << "moved to: " << z << endl;
			}
			
			// reset all information to zero for next ant
			for( k = 0; k < 32; k++ )
				city_traveled[k] = 0;
			path_counter = 0;
	
			cout << "reset info" << endl;
			
		}

		
		// evaluate paths
		//path_try = path_eval( paths, edges ); 	
		//if( path_try < path_best)
	//		path_best = path_try;
//		cout << "path eval" << endl;

		// time for next iteration!
		t++;
	}

	return path_best;
}

// evaluate path lengths
float path_eval( int paths[][31], Edge edges[31][31] )
{
	float path_best = 100000.0;
	float path_try = 0;
	int i, j, k, m = 0;
	int city1, city2;	

	// find path lengths for each ant
	for( i = 0; i < 32; i++)
	{
		path_try = 0.0;

		for( j = 0; j < 31; j++)
		{
			city1 = paths[i][j];
			city2 = paths[i][j+1];	
			path_try += edges[city1][city2].distance;
		}
		
		// compare path_try against best
		if( path_try < path_best)
			path_best = path_try;
	}	

	return path_best;
}

// calculate pheromone sum for untraveled edges
float sum_pheromone( int curr, int city_traveled[], Edge edges[][31] )
{
	int i = 0;
	int j = 0;
	float sum = 0;

	// find sum of pheromones on remaining untraveled edges from curr node
	while( i <  curr )
	{	
		if( city_traveled[i] == 0 )
		{
			cout << "traveled to: " << i << endl;
			sum += edges[i][curr-1-i].pheromone;
			cout << "sum: " << sum << endl;
			cout << "pheromone: " << edges[i][curr-1-i].pheromone << endl;
		}
		i++;
	}

	cout << endl << "i: " << i << endl;
	cout << "p1: " << sum << endl;

	while( i < 31)
	{
		if( city_traveled[i] == 0 )
			sum += edges[curr+1][j].pheromone;
		i++;
		j++;
	}
	
	cout << "i2: " << i << endl;
	cout << "p2: " << sum << endl;
	
	return sum;
}

// generate probabilty that ant will move to node
void prob_list( int curr, int sum_p, float probabilities[31], int city_traveled[], Edge edges[][31] )
{
	int i = 0;
	int j = 0;
	float alpha = 10.0;
	float beta = 0.0;
	float probability = 0;

	cout << "curr: " << curr << endl;

	while( i < curr )
	{
		if( city_traveled[i] == 0 )
		{	
			probability += ( pow(edges[i][curr-1-i].pheromone,alpha )*
				pow(edges[i][curr-1-i].visibility,beta))/
				(sum_p * pow(edges[i][curr-1-i].visibility, beta ) );
			probabilities[i] = probability;
		}
	
		else if( city_traveled[i] == 1 )
			probabilities[i] = probabilities[i-1];
		i++;
		cout << "i: " << i << " prob: " << probability << endl;
	}

	while( i < 32 )
	{
		if( city_traveled[i] == 0 )
		{	
			probability += ( pow(edges[curr+1][j].pheromone,alpha )*
				pow(edges[curr+1][j].visibility,beta))/
				(sum_p * pow(edges[curr+1][j].visibility, beta ) );
			probabilities[i] = probability;
		}
	
		else if( city_traveled[i] == 1 )
			probabilities[i] = probabilities[i-1];
		i++;
		j++;
		cout << "i: " << i << " prob: " << probability << endl;
	}

	//cout << "end prob fun" << endl;
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
	float path_best;

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
			xdist = pow( ( cities[i][0] - cities[j][0] ), 2 );
			ydist = pow( ( cities[i][1] - cities[j][1] ), 2 );  
			edges[i][j].distance = sqrt( xdist + ydist );
			edges[i][j].pheromone = 1.0;
			//edges[i][j].visit = false;
			edges[i][j].visibility = 1 / edges[i][j].distance;
		}
	}

	// cout << "after fill edge array" << endl;
	
	srand( time(NULL) );
	
	// run simple aco
	path_best = saco( 1, 32, edges );
	
	cout << "Best distance is: " << path_best << endl;
	// cout << "saco ran" << endl;


	// close file!
	fin.close();	
	
	return 1;
}

