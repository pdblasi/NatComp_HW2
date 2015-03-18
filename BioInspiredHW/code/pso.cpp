// Author: Stephanie Athow
// Date: 16 March 2015
// Professor: Dr. McGough
//
// Problem: "Fundamentals of Natural Computing", pg 260, #8
// 	Apply ths PS algorithm described in Section 5.4.1 to the maximization
// problem of Example 3.3.3.
//
// Code Credit: Dr. Jeff McGough, 
// 	Lecture Slides - Ch5: function prototypes and main

// Includes
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <math.h>

using namespace std;

// Defines
#define POP 20
#define STEPS 200
#define _USE_MATH_DEFINES

// Function Prototypes
void initswarm( double swarm[] );
void initvel( double vel[] );
void init( double swarm[], double bestind[], double fitbest[] );
void printswarm( double swarm[], double fitness[] );
void printvel( double vel[] );
double fitswarm( double swarm[], double fitness[] );
double fit( double x );

// Functions

// Main - runs the helper functions
// Author: Dr. McGough
int main()
{
	int i, j = 0;
	double swarm[POP], vel[POP], bestind[POP], fitness[POP], fitbest[POP];
	double best, top, phi1, phi2;

	srand( time(NULL) );
	initswarm( swarm );
	best = fitswarm( swarm, fitness );
	top = fit( best );

	//cout << "x = " << best << endl;	
	
	while( j++ < STEPS )
	{
		// update positions and re-evaluate
		for( i = 0; i < POP; i++ )
		{
			// acceleration constants
			phi1 = rand()%200/1000.0 - 0.1;
			phi2 = rand()%200/1000.0 - 0.1;
		
			// new velocity
			vel[i] += phi1*(bestind[i] - swarm[i]) + phi2*(best - swarm[i]);
			
			// prevent invalid velocities
			if( (swarm[i] + vel[i] > 0.0) && (swarm[i]+vel[i] < 2.0) )
			{
				swarm[i] += vel[i];
				fitness[i] = fit( swarm[i] );
			}
		}
		
		// update best fit for each individual and best individual
		for( i = 0; i < POP; i++ )
		{
			if( fitness[i] > fitbest[i] )
			{
				bestind[i] = swarm[i];
				fitbest[i] = fitness[i];
			}
			
			if( fitness[i] > top )
			{
				best = swarm[i];
				top = fitness[i];
			}
		}
	}

	cout << "Best is: " << best << endl;

	return 0;
}

// initialize particle positions
// Author: Stephanie Athow
void initswarm( double swarm[] )
{
	int i = 0;
	
	for( i = 0; i < POP; i++ )
	{
		swarm[i]  = ( rand()/ (double)(RAND_MAX) );
		//cout << "pos = " << swarm[i] << endl;
	}
	return;
}

// initialize particle velocities
// Author: Stephanie Athow
void initvel( double vel[] )
{
	int i = 0;

	for( i = 0; i < POP; i++ )
	{
		vel[i] = (rand() / (double)(RAND_MAX) );
	}

	return;
}

// initialize particle positions, find best individual and best fit
void init( double swarm[], double bestind[], double fitbest[] )
{
	return;
}

//print particle fitnesses
void printswarm( double swarm[], double fitness[] )
{
	return;
}

// print particle velocities
void printvel( double vel[] )
{
	return;
}

// determine each particle's fitness
// Author: Stephanie Athow
double fitswarm( double swarm[], double fitness[] )
{
	int i = 0;
	double best_eval = 0.0;
	double best_x = 0;

	for( i = 0; i < POP; i++ )
	{
		fitness[i] = fit( swarm[i] );
		//cout << "x: " << swarm[i] <<  " = " << fitness[i] << endl;
		
		if( (fitness[i]) > best_eval )
		{
			best_eval = fitness[i];
			best_x = swarm[i];
			//cout << "best " << endl;
		}
	}

	return best_x;
}

// Equation evaluation from example 3.3.3
// g(x) = 2^(-2((x-0.1)/0.9)^2) *( sin(5*pi*x) )^6
// Author: Stephanie Athow
double fit( double x )
{
	double exponent, fit;

	if( ( x > 0 ) && ( x < 1 ) )
	{
		exponent = -2 * pow( ( ( x - 0.1 ) / 0.9 ) , 2);
		fit = pow(2, exponent) * pow( (sin(5*M_PI*x)), 6 );
	}

	else
		fit = -10;

	return fit;
}


