#!/usr/bin/env python
# coding: utf-8

# ![11.png](attachment:11.png)

# <h5> Authors: Mathieu Nedelec, Alan Mccall, Christopher Carling,Gregory Dupont </h5>

# <h1> Recovery in Soccer </h1>

# <h3> Intro: </h3>

# <p> This study aimed to compare the recovery kinetics of physical performance and subjective ratings in response to a soccerspecific exercise simulation on natural grass and artificial turf. Physical performance tests and subjective ratings were
# assessed on 13 professional soccer players before, immediately after, 24 h and 48 h after the test. Physical performance tests
# included squat jump, countermovement jump, 6-s sprint on a non-motorised treadmill and isokinetic eccentric hamstring
# assessment </p>

# <p> These results suggest that a one-off
# exercise on artificial turf does not induce greater fatigue nor does it delay the recovery process when compared to natural
# grass among regular artificial turf players. </p>

# <h3>Comparisons between playing surfaces for physical performance and subjective ratings after a soccer-specific exercise simulation with the change expressed as relative values (%) for objective
# tests and absolute values (av) for subjective ratings (
# + 95% confidence intervals) and the magnitude of the change (effect size). </h3>

# In[9]:


import plotly.express as px

fig = px.line(x=["SJ","CMJ","HPT","MPO","MS","PS","Sleep","Fatigue","Stress","Soreness","TQR"], y=[0,0,0,0,0,0,-0.27,0.15,-0.31,-0.21,0.08], title=" Baseline - Effect Size")
print(fig)
fig.show()


# In[10]:


import plotly.express as px

fig = px.line(x=["SJ","CMJ","HPT","MPO","MS","PS","Sleep","Fatigue","Stress","Soreness","TQR"], y=[-0.34,0.04,-0.29,-0.03,-0.15,0.01,0,0.45,-0.15,0,0], title="0h - Effect Size")
print(fig)
fig.show()


# In[13]:


import plotly.express as px

fig = px.line(x=["SJ","CMJ","HPT","MPO","MS","PS","Sleep","Fatigue","Stress","Soreness","TQR"], y=[-0.09,-0.12,-0.29,0.17,0.13,-0.02,-0.40,0.11,-0.23,-0.13,0.26], title="24h - Effect Size")
print(fig)
fig.show()


# In[14]:


import plotly.express as px

fig = px.line(x=["SJ","CMJ","HPT","MPO","MS","PS","Sleep","Fatigue","Stress","Soreness","TQR"], y=[0.40,0.04,-0.43,-0.02,-0.04,0.05,0.43,0.27,0.07,-0.09,-1.19], title="48h - Effect Size")
print(fig)
fig.show()


# <h6> Some videos for the subject from diffrent sources </h6>

# In[24]:


from IPython.display import HTML

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/yt7tJlBpw9I?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>')


# In[23]:


from IPython.display import HTML

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/EE6mMsXdXAw?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>')


# In[ ]:




