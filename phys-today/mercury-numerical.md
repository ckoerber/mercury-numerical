# Numerical Simulations and General Relativity for High-School Students
## How you can introduce High-School Students to the basic concepts of numerical simulations and run their first computations including General Relativity -- in just one day

When I was in high-school, my biggest intrest were phenomena beyond the scope of what I currently knew.
Unfortunately, at this point, I did not yet have the theoretical toolset to dig deep.
But even though I was not able to compute things myself, I could grasp some insights of nature through visualisations.
With the growing availability of computational resources and accessibility to coding experience, it is a straight forward task to let students run their own simulations.
In this article we talk about our experience of teaching the basics of numerical simulations in a playfull way to high-school students.
The working case is the classical planetary motion of mercury and the modifications to it's orbit coming from general relativity, which has long been a source of fascination not only for trained physicists, but also for the general public.
This example is particular motivating in the era where we have developed a new, additional sense for astronomical observations through gravitational waves.

This article is accompanied by a publication in which we describe the content of a one-day course.
The first idea for this course originates from a school project work in 2014 of one of the publications author, J. Heuer, when she was in 11th grade.
Only one year later it was adapted and introduced as a course in the "Schülerakademie Teilchenphysik 2015" ("Student Academy for Particle Physics") which aims at high-school students from 10th to 13th grade.
It usually has about 25 participants, which come from all over Germany (during their vacations), and takes place biannually at the Science Center Overbach in Jülich.
During the four days of academy the students take part in different activities:
* lectures on various topics in particle physics,
* a tour of the particle accelerator COSY and 
* a visit to the high-performance computing facility at the Research Center Jülich.
At the end of the course, the last day is dedicated to hands-on work where studentes have three different choices: one choice being about coding numerical simulations for a physics system.

IMAGE COURSE

The reason why it was desired to offer a course on numerical simulation is the relevance of simulations in active research.
Simulations are often the best method available for obtaining quantitative results in not only physics.
From NEURONS IN BIOLOGY OVER ATOMS IN CHEMISTRY THROUGH the descriptions of Quarks and Gluons through Lattice Quantum Chromodynamics.
However, in most school curricula, even though students learn about physics and can enjoy classes on programming, both topics are seldom combined.
Albeit we see a big opportunity in this approach:
students can experience and experiment with physics systems that otherwise can only be studied theoretically, while, at the same time, they can pick up valuable skills in programming.

#### IM HERE

Here the students worked in pairs charing one laptop with the necessary software, VPython, preinstalled.
We, the authors, acted as supervisors for the students and the feedback we got was enthusiastic.
Thus this course became a permanent part of the academy.

Before outlining the course, a few words on VPython: VPython is ideally suited to introduce students to programming, since it lets the students nicely visualize their results in 3D animations through very simple code.
Also it is very practical as it is easy to install on all platforms.
In the academy for example we start the course by working through the "ball in the box" example - a very simple program, that already demonstrates all the necessary features of VPython.

The basic outline of the course is at follows: First, the students visualize the orbit of one planet around a stationary sun as it arises from classical newtonian mechanics.
Here they learn a basic concept of simulations: discretisation.
The orbit is derived by taking small but finite time steps and at each step calculating the position, velocity and acceleration from the one before using Newtons second law.
The students arrive at the typical elliptic curves, which are fixed in space.
In particular the point of closest approach to the sun, the perihelion, does not move.
In figure 1 you can see an example of the output of VPython. 

Figure 1: Mercury orbit from newtonian gravity.

These closed curves are actually a consequence of the 1/r potential we have in newtonian gravity.
To allow for movement of the perihelion the students need to modify the potential by including terms proportional to 1/r2 and 1/r3. (see figure 2).
In our one day courses, this is how far all students, indepedendent of their prior knowledge in programming or differential calculus, managed to get.
Many students then continued to extract the value for the perihelion motion.
The final step is the comparison of the calculated value with the measured one.
Since the corrections due to general relativity are extremely small, the students need to interpolate their results to these small values.
This completes the basic course.

Figure 2: Orbit with perihelion motion.

By the way, the result of the simulation is a change of 0.104'' = 0.104/3600° in the perihelion for each revolution which means that in 100 earth years, the length axis of the mercury orbit should rotate approximately by 42.3'' = 0.01º.
The observed perihelion motion of Mercury is nowadays determined as (574.1 ± 0.65)'' per 100 earth years, which at first glance seems to deviate quite a lot from the simulation result.
However the bulk of this number is due to interactions with the other planets.
The part, that is unexplained by newtonian gravity is only (42.56 ± 0.94)” and this matches perfectly to the simulation.

We feel that at this point we have a very well rounded course.
The students learned the basics of numerical simulations in physics, extended newtonian physics to include effects of general relativity and then get a value for the perihelion motion, that matches the real measured value.
One point, that we could not sufficiently cover in the summer school, is the discussion of the errors.
These occur in simulations due to the finite time steps.
On a basic level this does indeed happen almost automatically, since the students, especially if encouraged, tend to play with the given values.
Then they find that when they choose the time steps too big, their trajectories will become somewhat angular and the orbits won't close properly.
Thus it becomes clear, that larger time steps induce larger errors.
However for those which have the luxury of more time for this project, we included another section in our paper which shows how a detailed discussion could be managed.

All in all we had a very positive resonance.
Out of three projects in the summer school roughly half of the students tend to choose this one. 
The students had very different levels of prior knowledge. Roughly half had programing experience and most had already learned about derivatives in school.
However this open course seems ideally suited to accommodate for these circumstances.
Furthermore it was very interesting to see, that the students had quite different interests.
While some pushed to solve increasingly difficult physical problems (e.g. including a third body and sometimes even turning the resulting planes against each other which we did not even think about), others where more interested in exploring the limits of their current simulation (preferably creating increasingly chaotic trajectories) and others liked to improve upon their graphical delivery.
All in all they came up with many valuable ideas to improve our simplistic original design.
In the breaks we often observed them bringing in the students from other projects to explain what they had done and show them the results of their efforts.

Due to these very positive results we decided to make this course available to a broader public.
We believe it is ideally suited not only to complement the standard curriculum, but also for example for extra curricular working groups running for a longer period.
We hope it will help to inspire students to keep on learning about and exploring the fascinating physical phenomena that govern our world.









