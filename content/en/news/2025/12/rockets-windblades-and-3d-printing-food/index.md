---
title: Rockets, windblades, and 3D-printing food, with Matt Thomas aka LT72884
date: 2025-12-12
authors: Aleksandr Prokudin
draft: false
categories: showcase
tags:
  - research
  - interview
  - CFD
  - FEM
cover:
  image:
  caption:
---


People have been using FreeCAD in academia and research for many years, and the range of these research projects is surprisingly broad.

Today, we are talking to Matt Thomas aka LT72884, who has a great [YouTube channel](https://www.youtube.com/user/LT72884/) where he explains how to use free and open-source engineering software for rocket design, CfD simulation, FEM, and data analysis.

{{< youtube id=vPwkIOQAOQ4 title="Complex CFD with Complex geometry on Freecad and Ondsel" loading=lazy >}}

**Hi, could you please briefly introduce yourself?**

Yeah, sure. My name is Matt Thomas, and I am very passionate about science and engineering. I grew up with a mother who was a head nurse and team lead for the first heart transplant, as well as a team member of the Human Genome Project, so science and medicine were a very common dinner table conversation for me growing up.

My dad, on the other hand, was a telecommunications specialist for the military, and he would bring me along for some of his jobs, such as installing very large phone systems for the base and the research facility at the local university.

When I was in high school, I learned about computer networking and web design because I was _horrible_ at math and science. I fell in love with technology, and after graduating in 2003, the local university had a sister program with Carnegie in Network Engineering and cybersecurity. I received my CCNA, CCNP, RHCT, Ethical Hacking, and a few other well-known certifications, as well as a Bachelor's degree.

However, when I was claiming graduation, something just didn't feel correct. So, I had a long and excellent conversation with my mother, who has never led me down the wrong path. She suggested that I have always liked science _and_ technology, so maybe there is a way to combine the two. So I did just that.

I was 26 years old when I decided to go back to school for medicine and engineering, the only problem was... I had 3 years of basic math to make up before I could even apply for the associate of pre-engineering and my microbiology coursework.

After 3 years, I finally made it into the program and continued to push through 6 more semesters of math, 3 semesters of chemistry, biology, pathophysiology, and microbiology. Then I transferred to another university where I finished my degree in Aerospace engineering with a masters coursework in Computational Fluid Dynamics (CFD), numerical and data analysis, as well as advanced material sciences.****

**This is your second higher education, right? Why did you choose engineering?**

To be honest, I chose engineering to honor my family and mom. I grew up in a Christian home, so I was always curious how the big guy in the sky organized things. I consider him to be the ultimate engineer and scientist, as did my mother.

Engineering and science help me understand how things in this world and out of this world work. I love to just know how things operate, even if I never use that device or product. Oh, and the world is not flat :)

**How many papers have you already published where free and open-source software is used prominently?**

I have about 8-10 papers using open source software as the predominant applications, such as [QBlade](https://qblade.org/), [OpenFAST](https://www.nrel.gov/wind/nwtc/openfast), [MLife](https://www.nrel.gov/wind/nwtc/mlife), [Octave](https://octave.org/), FreeCAD, Ondsel Engineering Suite, [OpenFOAM](https://www.openfoam.com/), [ParaView](https://www.paraview.org/), [PrePoMax](https://prepomax.fs.um.si/), and [Fatlab](https://sourceforge.net/projects/fatlab/) (an open-source fatigue analysis tool), with verifications done with ANSYS.

Many of the papers deal with wind turbine durability and fatigue analysis (["Estimating Wind Turbine Blade Durability Utilizing National Renewable Energy Laboratory Tools"](https://www.researchgate.net/publication/382689796_Estimating_Wind_Turbine_Blade_Durability_Utilizing_National_Renewable_Energy_Laboratory_Tools?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6Il9kaXJlY3QiLCJwYWdlIjoicHJvZmlsZSIsInByZXZpb3VzUGFnZSI6InB1YmxpY2F0aW9uIn19) is the latest) and can be found on [ResearchGate](https://www.researchgate.net/profile/Matt-Thomas-22). Some of them may have similar titles and information, but they are extensions of our original work, meaning, we published a paper, then completed even more work, and added to it for a second publication and peer review. I even wrote a basic 75-page user manual for OpenFAST so that anyone wanting to learn how to use it can.

**Why is it important for you to rely on free/open-source tools?**

First, they are available to research students and interns, or anyone, for that matter, for a really _good_ price. Second, open-source engineering tools are very important, especially for developing nations that can not afford the drastic price tag of some packages. However, people are skeptical of using open-source software because they are afraid it's "unsafe" or will produce inaccurate results. This is why having NASA perform validation tests with OpenFOAM was such a _huge_ deal for the open-source community.

**How did you get involved with rockets?**

It was an internship and practicum at school. We were tasked with creating an active drag system for a rocket to achieve a specific altitude. They are like air brakes in a sense, and from there, I just kept learning more and more about rockets, which led to formulating and characterizing my own solid rocket fuel using ammonium perchlorate, metals, and epoxies, the same ingredients they use for much larger rockets.

{{< youtube id=TnYmVRv1RdM title="Part 4 Force calculations CFDOF Ondsel Engineering Suite" loading=lazy >}}

**And then you got hooked?**

I have always loved planes, and I often go to the aerospace museum that is close to my home.  When the school offered me and a few others this chance, I took it and have loved it ever since. Making my own rockets, fuel, and seeing them go from digital concept to reality is very rewarding.

**I've also noticed that **[**wind turbines and their **](https://www.researchgate.net/publication/382689796_Estimating_Wind_Turbine_Blade_Durability_Utilizing_National_Renewable_Energy_Laboratory_Tools?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InB1YmxpY2F0aW9uIiwicGFnZSI6InByb2ZpbGUiLCJwcmV2aW91c1BhZ2UiOiJwdWJsaWNhdGlvbiJ9fQ)<span style="box-sizing: border-box; margin: 0px; padding: 0px;">[**durability**](https://www.researchgate.net/publication/382689796_Estimating_Wind_Turbine_Blade_Durability_Utilizing_National_Renewable_Energy_Laboratory_Tools?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InB1YmxpY2F0aW9uIiwicGFnZSI6InByb2ZpbGUiLCJwcmV2aW91c1BhZ2UiOiJwdWJsaWNhdGlvbiJ9fQ)</span>**are a big deal for you. How did the interest originate?**

Someone from the state research department on wind energy read my design thesis on high-powered rockets, which included a lot of testing and analysis. So they asked me if I wanted to join the team for a few months as a full-time job doing fatigue analysis and design for wind turbines. I said, "Sure, why not?". The job lasted 2 years because they really liked my work and how I handled things.

{{< youtube id=33IqCq0UnQE title="How to use OpenFast wind turbine simulation software" loading=lazy >}}

**You use a whole variety of tools: OpenRocket, FreeCAD, the CfdOf workbench and OpenFOAM, Paraview, OpenFAST, MLife, and even Excel. That's a lot of bridges to build between applications. How well does it work for you, and where do you think are the worst integration bottlenecks today?**

So far, I have not had any issues exporting/importing data from one application to the other. Paraview plays very nicely with OpenFOAM data, and the integration of ParaView into the CfDof workbench for FreeCAD has been nice, though I prefer to close FreeCAD after every CFD simulation and open the data into a fresh start of Paraview.

I actually use [pyDatView](https://github.com/ebranlard/pyDatView) from GitHub as a way to view some of the OpenFOAM data files. It's an old tool that I just discovered.

{{< youtube id=Ynb23fo9lbI title="Using pydatview and excel to make force graphs from openfoam data" loading=lazy >}}

OpenFAST and MLife both export the data as Excel files, so that makes it very nice. I do not use LibreOffice Calc as it is missing a few major functions needed for most engineering workflows. This is why I use Excel. Their solver and numerical methods are excellent

OpenRocket is one of my favorites, but it is a standalone software. It will calculate the forces and drag coefficients for you based on the Barrowman Equations developed by James Barrowman at NASA. Using just geometry, the Reynolds number, and skin friction values. OpenRocket will allow you to graph _many_ values against each other, making it a very valuable tool if CFD is not an option.

Now, speaking of CFD, I have set up _many_ simulations (again, thanks to the forums for helping me get the preliminaries setup) of high-powered rockets to test against OpenRocket, and sure enough, I get pretty dang close to the same values.

Most people, when they do CFD for the first few times, get results that are way off, and then they get discouraged. 95% of the time it's because they have too coarse of a mesh and not enough refinement areas for the mesh to accurately produce good results. This is why I made the YouTube series on CFD with Ondsel/FreeCAD.

Well, my primary reason is so I don't forget how to do it myself. I record a lot of things I do so I can reference them later, which comes in handy if a supervisor asks about a process.

As for bottlenecks, OpenRocket, an advanced simulation tool, is much harder to use and integrate with other software. PrePoMax actually works better as a standalone product, i.e., import the STP file, mesh it, then set up the scenario, all in PrePoMax. That is one bottleneck. The other is that FreeCAD needs to improve the meshing defaults in the FEM workbench. PrePoMax has _killer_ defaults and meshes extremely well, we just need that in FreeCAD now.

{{< youtube id=I8pgxxt1pD8 title="FreeCAD FEM with Boolean Fragments" loading=lazy >}}

**When we first discussed your academic work, you said that the paper that you presented at the IEEE conference in May 2024 was well-received, especially from other countries and developing nations, and that was your focus. Could you please elaborate on the focus part?**

For sure : ) My main focus at that presentation was to spread the word on how reliable FreeCAD, OpenFOAM, OpenFAST, and MLife are for major engineering projects. I mean, I had been doing stress-testing and designing 65-meter to 100-meter wind turbine blades in FreeCAD with ease(thanks to the advice from the forums when i got stuck), and then performing all CfD, FEM, and stress analysis with FreeCAD and OpenFAST/MLife.

Being a developing country and feeling lost in how to begin projects due to high-cost software is very stressful. I have wanted to share this knowledge, and why not share it at a very large IEEE event?

As soon as I finished my presentation, I had 3 or 4 attendees come over and ask for copies of all my papers to take back to their countries to share with officials they knew.

**Have you been in touch with them ever since?**

I have tried a couple of times over the last year, and have not heard anything back. Could be due to internet laws in their country, which could prevent communication.

**When you talk to your mates at university and to your teachers, do you see much antagonism towards free and open-source software? If you do, where do you think it is coming from?**

Yes and no, but mostly no! My professors encourage the use of open-source software to teach us how to validate our results. We then share our own personal results with about 30 other students and 4 other professors for review. It's an excellent way to teach new students the importance of peer review and safety.

I think the biggest frustration with FreeCAD that users and university students have is the workarounds that we have to do often to get 3 common features to work, such as thickness, fillet, and chamfer, but that is an issue to do with the kernel, which FreeCAD does not manage unfortunately.

My fluids professor uses OpenFOAM and prefers it over others because it requires students to understand the theory of fluid dynamics rather than just pushing buttons. Anyone can push buttons and get data back, but, like he says, "Garbage in is garbage out", or GIGO for short. I still prefer to push buttons, I know the theory, and now I like to just push a button and let the PC do all the work.

Where the antagonism comes from is the data science group, and I don't blame them. As I previously mentioned, LibreOffice Calc and other open-source spreadsheet programs lack some major functions, such as a non-linear solver that actually works without wasting time with some sort of workarounds.

**What's the next big chapter for you research-wise?**

In the last 4 years, I published a few papers on food-safe 3D printing. I'm currently doing the last extension of the [original paper](https://www.researchgate.net/publication/389100627_Innovations_in_Sanitization_for_3D-Printed_Parts_in_Medical_and_Critical_Applications), testing filaments for toxins and heavy metals via leach, migration, and mass spectrometry testing.

My first publication on this matter illustrated that layer lines do not pose a risk and can be cleaned and sanitized to safe levels, and that nozzles do not leave any lead either.