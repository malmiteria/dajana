# dajana
a programming language with good UX


## My Goal
I wanna design a programming language with good UX. This means a few things :
 - listing a few important use cases
 - reading over pros and cons of multiple langages solution (if any) to those use cases
 - evaluating the UX of those solutions
 - designing my own solution, based on what i learnt (and evaluating it too).
 
I will mostly back my UX evaluation based on this [french resource](https://www.usabilis.com/le-guidage-criteres-ergonomiques-de-bastien-et-scapin/#:~:text=Quatre%20sous%2Dcrit%C3%A8res%20participent%20au,d%C3%A9finition%20de%20l'ergonomie).
which in english translates to this list or criteria (translated on reverso):
1. Guidance
   1. Inducement
   2. Grouping / Distinction between Items
      1. Grouping / Distinction by location
      2. Grouping / Distinction by format
   3. Immediate Feedback
   4. Readability

2. Workload
   1. Brevity
      1. Conciseness
      2. Minimum Actions
   2. Information Density

3. Explicit Control
   1. Explicit Actions
   2. User control

4. Adaptability
   1. Flexibility
   2. Consideration of User Experience

5. Error Management
   1. Protection against Errors
   2. Quality of Error Messages
   3. Correction of Errors

6. Homogeneity / Coherence

7. Meaning of Codes and Denominations

8. Compatibility


I will also mostly back my listing of use cases on my real life experience as a developper, using knowledge managment interview techniques.


## The use case i'm faced with as a web developper, or the things i do and how i go about it

 - add / remove / modify some behavior of the program i'm writing, by adding, removing, modifying code, or adding appropriate libraries
 - try to understand what the code does today, by reading it, running it myself, or asking coworker to explain their codes
 - try to make sure i don't accidentally remove features / reintroduce bugs, by adding automated tests on those features and bugs (the behavior of the program i know i want or don't want), when i work on those bug / features
 - catch bugs, by adding tools on production environment such as sentry to collect and display crash reports
 - remove bugs discovered in production, by first reproducing them locally, then in some test scenarios
 - ensure everyone in the team, even new hires, can read / understand my code, with minimal interaction on my part, by refactoring my code, meaning, in this order :
   - properly naming variables / functions / objects in a way that explains what they do or don't. Hopefully, this means when someone else tries to understand my code, they can read it, and it's enough. No need to run the code (or the tests), or to ask me what it means.
   - adding comments (even tho it's easy to forget to update those once the feature changes, so they aren't 100% accurate)
   - writing docs (even tho, not everyone always read it or know where to find it)
 - allow myself to work and break everything without breaking anything for users, by using multiple environment, one for development, one for production (the one given to users) and possibly some in between, to ensure the program works not only on my computer, for example, or for pre release, so team members can experiment with the feature, to make sure it's what was asked for
 - try to reduce time and effort needed to do any common and repeatable tasks (install the program, run it, test it, and so on) by scripting those actions.
 - ensure that i can add features / remove bugs in the future, by refactoring my code, meaning:
   - ensuring that my code is easy to read, so i can understand it enough to work on it
   - ensuring that different component of my program are minimally tied to one another, and not too dependant on one another, so each component is easier to reuse, or replace
   - ensure that the most common changes need the least amount of work on my part (DRY for example)
 - ensure that my work doesn't prevent anyone else from working too, by working on branches on git or equivalent tool
 - ensure that i can rollback fairly easily (so i can get back to a non buggy version if i end up stuck with new bugs for example), by commiting often on git or equivalent tool
 - ensure that the code i publish to the rest of the team, and or or users, is tested, and with good enough quality, by using automated CI to run tests and over scripts automatically on push
 - ensure that i can deploy farily easily new version on production by scripting the deployment steps, and possibly using tools such as docker to package my program, and render it independant on hardware / software setups
