# Physics simulations for high-school students

## Students program their first physics simulations demonstrating effects of general relativity—in just one day.

Today, numerical simulations have become a part of physicists’ everyday work and are often the best method for solving complicated problems that deal with fundamental building blocks of nature.
When we look back at our high-school years, we realize that having a physics education coupled with numerical methods programming at such an early stage would have been extremely beneficial.
Sadly, such a coupling of fields is rarely done, even in today's high schools.

In 2014 one of our collaborators, Joseline Heuer, conducted a school project in which she analyzed the motion of planets in the solar system through a simulation that included post-Newtonian effects.
The next year, we adapted her project to create a course for the ["Schülerakademie Teilchenphysik"](https://crc110.hiskp.uni-bonn.de/index.php?id=327) ("Student Academy for Particle Physics") held at the Science Center Overbach in Jülich, Germany.
The weeklong academy takes place every two years and is tailored toward high-school students age 16 to 19 from all over Germany.
It offers activities such as lectures on various topics in particle physics, a tour of the particle accelerator COSY, and a visit to the high-performance computing facility at the Jülich Research Center.
On the last day of the course, students choose to participate in one of three hands-on projects.
One was our numerical simulations course.

![Image of course](course.jpg)
Figure 1: Image of course

The main task of our course is to simulate the motion of Mercury around the Sun.
We start with the two-body system of planet and star governed by classical Newtonian mechanics only.
Here we teach the students about discretization as a basic concept of simulations.
The students solve an equation of motion numerically by picking a starting position and velocity of Mercury (the Sun starts at the origin with zero velocity) and then, employing Newtonian gravity as the force, evolving the position and velocity of Mercury in time with a finite number of steps.
The result is a planet that moves in either a parabolic open curve or an elliptic closed curve depending on the initial conditions.
In both cases, the curves are fixed in space, in particular the perihelion, the point of closest approach of the planet to the Sun, does not move.
Figure 2 shows an example of an elliptical orbit.

![Mercury orbit around the Sun from Newtonian gravity](orbit-wo-GR.gif)
Figure 2: Mercury orbit around the Sun from Newtonian gravity.

The fixed perihelion is a consequence of the use of the simple Newtonian 1/r2 gravitational force (with r as the distance between the Sun and Mercury).
In reality, the perihelion of Mercury’s orbit moves around the Sun over time, which is attributed largely to the influence of the other planets.
Already in 1859, long before the rise of computers, astronomers calculated the planetary influences through painstaking calculations and were able to describe more than 90% of the observed movement.
The rest was taken as evidence for an as yet undiscovered planet.
It was not until much later, when Einstein published his theory of general relativity (GR), that the remaining perihelion motion was really understood.

The goal of our course is to show students how to simulate the influence of GR.
Luckily, despite the complexities of the underlying mathematics, a simple approximation of GR can capture most of its effects.
We approximate the GR-induced force by including terms proportional to 1/r3 and 1/r4 in addition to the Newtonian 1/r2 term.

The actual perihelion motion due to GR is less than 42.3” (0.011°) in a century.
However, the students could produce animations like the one in figure 3 by experimenting with unphysically large strengths of the additional terms.

![Mercury orbit around the Sun from Newtonian gravity including GR additions](orbit-w-GR.gif)
Figure 3: Mercury orbit around the Sun from Newtonian gravity including GR additions.


Our program employs [Python](https://www.python.org/) as a programming language and [VPython](http://vpython.org/) for graphical output.
Both are easy to learn, even for those without programming experience.
We start the course by briefly introducing the coding language and explaining the basics of differential and vector calculus as this is needed to understand the position and velocity update procedure.
By the end of that tutorial, all the students, regardless of previous knowledge, should be able to produce the simulations.

During the main part of the course, we give only basic guidance, we help out only when needed, and we encourage the participants to pursue their own ideas.
We start out by providing a basic [code template](https://github.com/ckoerber/perihelion-mercury/blob/master/py-scripts/template.py), which defines physical and numerical parameters, sets up the visual display and highlights the basic structure of the final program.
Using this template, the students initialize the visualization objects, implement a function for the position and velocity update and write a loop to evolve the orbit.
At the 2015 student academy, the students explored the problem in groups of two.
Some students focused on the GR part, while some played with the parameters of the system (masses, size of the time step, etc.) and explored the boundaries of the solution in terms of stability.
Others tossed in an additional planet, sometimes with a tilted orbital plane, and observed the chaotic nature of the three-body problem.
Still others improved the graphical output by, for instance, marking the position of the perihelion—an idea we borrowed for later courses.

During breaks the students excitedly showed their results to the participants of the other two projects and explained their efforts, motivations, and results.
Even after the course we had some interesting discussions on the theories of relativity, with the students pushing us toward, and sometimes beyond, the limits of our own knowledge.
Due to the interest and positive feedback, in 2017 we offered a second, refined installation of the course, with similar results.

We recently made the course publicly available in [our paper](https://arxiv.org/abs/1803.01678).
The course at the science academy lasted for one day.
In our paper we provide additional material on analyzing numerical errors and extracting the  perihelion motion for natural GR forces.
This should allow for a longer more in-depth project for interested students.
We will continue to offer the course at the academy in the future and hope that others will have the same success and fun that we had.

Christopher Körber is a member of the Institute of Advanced Simulation at Forschungszentrum Jülich, Germany.
He has finished his PhD in nuclear physics at the University of Bonn in 2018.
His scientific interests range from numerical simulations over data analysis and visualization to the presentation of scientific content.

Jan-Lukas Wynen is a PhD student at the Institute for Advanced Simulation at Forschungszentrum Jülich and the University of Bonn.
He simulates and analyzes strongly correlated quantum systems.
His scientific interests are focused around numerical simulations including development of algorithms and scientific software.

Inka Hammer is a PhD student at the Forschungszentrum Jülich where she is working in the field of hardonic physics, in particular on the interplay of hadronic molecules and heavy quarkonia.
She received her master degree in physics from the University of Bonn in 2016.

We would like to thank Joseline Heuer, Christian Müller, and Christoph Hanhart for introducing us to this course, for providing the required framework at the "Schülerakademie Teilchenphysik," and for the help in writing this article.
