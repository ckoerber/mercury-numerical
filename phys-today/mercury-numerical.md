# Numerical Simulations and General Relativity for High-School Students
## How you can introduce High-School Students to the basic concepts of numerical simulations and run their first computations including General Relativity -- in just one day

_What about title?_

When I was in high-school, my biggest interest were phenomena beyond the scope of what I currently knew.
Even though at that point I did not yet have the theoretical toolbox to dig deep, I could gain some insights into nature through visualizations.
Since then, numerical simulations have become part of my every day work.
They are often the best method to solve complicated problems such as describing particles in my work as a physicist.
Unfortunately, physics education was rarely combined with programming in school in my time and little has changed since.

In 2014 on the authors of our publication, J. Heuer, did a school project for which she simulated the motion of planets in the solar system.
The next year, we adapted her project to create a course for the "Schülerakademie Teilchenphysik" ("Student Academy for Particle Physics") at the Science Center Overbach in Jülich, Germany.
The week long academy takes place every two years and aims at high-school students from grade 10 to 13 (age 16 to 19) from all over Germany.
It offers several activities such as

* lectures on various topics in particle physics,
* a tour of the particle accelerator COSY and
* a visit to the high-performance computing facility at the Research Center Jülich.

At the end of the course, the last day is dedicated to hands-on work where students have three different choices.
One of those was our numerical simulations project.


Figure 1: Image of course


The main task of the course was to simulate the motion of Mercury around the Sun using classical Newtonian mechanics.
Here we taught the students about discretization as a basic concept of simulations.
The only way we can solve an equation of motion numerically is by picking a starting position and velocity and evolving them in time with finite number steps.
The result are the typical elliptic curves fixed in space that are shown in figure 2.


Figure 2: Mercury orbit around the Sun from Newtonian gravity (GIF).


We did not stop there but only used this simulation as a first step.
One particular feature of the simulation is that the point of closest approach to the Sun, the perihelion, does not move which is a consequence of the 1/r gravitational potential we have used so far.
In reality, however, the perihelion moves around the Sun over time, which was known for a long time and attributed the the influence of the other planets.
Astronomers calculated this influence over several years in painstaking manual labor (this was long before the rise of computers) and were able to describe more than 90% of the observed movement.
The rest was taken as evidence for an as yet undiscovered planet.
It was not until much later when Einstein published his theory of general relativity that the remaining perihelion motion was really understood.
In fact this was one of the big successes of the new theory helping it gain popularity.

Our goal was to show the students how to simulate this influence of general relativity.
At first this seems like an impossible task given that general relativity is mathematically very complicated.
Luckily a simple approximation can capture most of the effects.
This approximation is simply adding terms proportional to 1/r² and 1/r³ to the Newtonian 1/r potential (r is the distance between Sun and Mercury).
The actual perihelion motion due to general relativity is less than 42.3″ = 0.011° in a century, so in order to be able to see anything the students played with the strengths of these additional terms.


Figure 3: Mercury orbit around the Sun from Newtonian gravity + general Relativity(GIF).


We chose [Python](https://www.python.org/) as a programming language and [VPython](http://vpython.org/) for graphical output.
Both are easy to learn even without programming experience and we started the course with a quick introduction to them.
We also spend some time explaining basics of differential and vector calculus.
This allowed all students to produce simulations even though they had different backgrounds and previous knowledge.

During the main part of the course, we gave only basic guidance and helped out where needed.
For the most part, the students could explore the problem on their own in groups of two which lead to many different solutions and extensions of the project.
Some students did not look at the general relativity part but instead played with the parameters of the system (masses, size of the time step, etc.) and explored the boundaries of the solution in terms of stability.
Others added an additional planet and sometimes even tilted the orbital planes and observed the chaotic nature of the three body problem.
Again other improved the graphical output by for instance showing the position of the perihelion - an idea we eventually picked up for later courses.

During breaks the students were excited to show their results to students from other projects and explaining efforts, motivations and results.
We also had some interesting discussions in the breaks and after the course on the theories of relativity with the students pushing us the limits of our knowledge.
Due to this and the positive feedback we received, we decided to offer a second, refined installation of the course in 2017 with similar results.

Now we would like to make the course publicly available in our paper [cite!].
The course at the science academy lasted for only one day which was a tight schedule.
In our paper we provide additional material on analyzing numerical errors and extrapolating the perihelion motion to physical values.
This should allow for a longer more in-depth project for interested student.
We will continue to offer the course at the academy in the future and hope that others will have the same success and fun that we had.
