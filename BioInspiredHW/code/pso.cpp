// Author: Stephanie Athow
// Date: 16 March 2015
// Professor: Dr. McGough
//
// Problem: "Fundamentals of Natural Computing", pg 260, #8
// 		Apply ths PS algorithm described in Section 5.4.1 to the maximization
// problem of Example 3.3.3.
//
// Code Credit: Dr. Jeff McGough, Lecture Slides - Ch5, headers and main

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
int main()
{
	int i, j = 0;
	double swarm[POP], vel[POP], bestind[POP], fitness[POP], fitbest[POP];
	double best, top, phi1, phi2;

	srand( time(NULL) );
	initswarm( swarm );
	best = fitswarm( swarm, fitness );
	top = fit( best );

	while( j++ < 500 )
	{
		for( i = 0; i < POP; i++ )
		{
			phi1 = rand()%200/1000.0 - 0.1;
			phi2 = rand()%200/1000.0 - 0.1;

			vel[i] += phi1*(bestind[i] - swarm[i]) + phi2*(best - swarm[i]);
			if( (swarm[i] + vel[i] > 0.0) && (swarm[i]+vel[i] < 2.0) )
			{
				swarm[i] += vel[i];
				fitness[i] = fit( swarm[i] );
			}
		}
		
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


// Equation evaluation from example 3.3.3
// g(x) = 2^(-2((x-0.1)/0.9)^2) *( sin(5*pi*x) )^6
double fit( double x )
{
	double exponent, fit;
	
	exponent = pow( ((-2) * ( x - 0.9 ) / 0.9 ) , 2);
	fit = pow(2, exponent) * pow( (sin(5*M_PI*x)), 6 );

	return fit;
}


