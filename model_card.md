# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

MusicBox v1.0

---

## 2. Intended Use

Music box is a program for users that are looking to find new music to listen to that is similar to their personal preferences. Taking into considering their genre, mood, energy level, and whether or not they like acoustic songs, MusicBox will present a user with a list of new songs to listen to. MusicBox will sometimes take into account one preference more than the others and assume the user will like a genre of music because of energy levels or acoustic preferences. A more realistic expectation would be that genre is the largest driving factor.

## 3. How the Model Works

By obtaining a users favorite genre, mood, energy level and acoustic preference, MusicBox weighs each point of data separately (genre gets 4pts, mood gets 3, energy level = 2 and acoustic preference is 1pt). Using a "master total", MusicBox then goes through the songs.csv file and finds songs that have the smallest difference between their (the song) points, and the users "master total" of points.

## 4. Data

There are 18 songs in the catalog with varying genres, these include pop, lofi, country, blues, jazz, rock, ambient, synthwave, indie pop, metal, hip-hop, r&b, electronic, folk and classical. Songs 11-18 on the list were added after to broaden the dataset for testing and use purposes. There are plenty of "niche genres" that are missing and would benefit the program greatly as this is one of the main weaknesses of the design, users with preferences that aren't accounted for are underserved and most likely wouldn't enjoy MusicBox.

## 5. Strengths

If a user has a common genre preference, MusicBox is very good at keeping on track with other relevant data points such as mood and energy level. Another point of note is that high-energy users are also served appropriately and will more than likely enjoy their recommendations. A result that I would have expected was the country user result, in my personal experience, people who enjoy Country music do not venture far away from their tempo or themes of their music.

## 6. Limitations and Bias

    This program has one major bias that could impact its' success. There are moods and genres that aren't accounted for and this could lead to a decline in users once found. Any user that prefers a niche-genre is going to be underserved and users who input a more rare mood is going to be underserved, anyone with the combination of the two would be recommended hardly anything. After these preferences are taken into account, their recommended list would be entirely dependent on energy and acoustic preference.

## 7. Evaluation

How you checked whether the recommender behaved as expected.

Prompts:

- Which user profiles you tested

Profiles that were tested were "consistent" users, such as a user that likes blues, being relaxed with low energy and likes acoustic. This would be an exmaple of a user whose energy matches the sound of their music. Outisde of that users with differing preferences were also tested such as a hip-hop preference but a target_energy on the lower side, but hip-hop is a genre where the tempo varies greatly.

- What you looked for in the recommendations

What I was looking for was a decrementing Score for each song that was more linear, this would be indicative of an aligned program with regards to its dataset, user profiles and recommendation functionality.

- What surprised you

A surprise to me was in certain users such as the blues enjoyer, their list of recommendations had a big drop off in score after the 3rd recommended song. Song #3 on the recommended list had a score of 7.37 and #4 had a score of 4.52, almost halving the song prior. This was later to be explained by the fact that the blues genre is a little more niche and these users were underserved by the dataset.

- Any simple tests or comparisons you ran

The weight of the importance of the energy prefernence was doubled, this had little to no effect on which songs were recommended but it did increase the Score by 1.5-2x which was interesting seeing that the weight was also doubled, seems to be a correlation there.

---

## 8. Future Work

I would broaden the genre list as a definite, this seems to be one of the causes of a main weakness in MusicBox. I would also like to add a bit more complexity to the recommendation functionality as there were cases of large gaps in score rating within a users 5 song recommendation list, sometimes even seeing a disparity of almost half between song #3 and song #4 in the list. I wouldn't be opposed to taking some tips from other recommendation software programs either, MusicBox isn't the first of its kind after all.

## 9. Personal Reflection

This was a great project, I apologize if it seems a bit frantic, my life has been hectic the past two or three weeks, but this was a fun one. I never actually thought about recommender programs too deeply, occasionally on my way to work I would envision them being a linked list using similar data points as this program but the amount of mathematics that are in things like Spotify or AppleMusic piques my interest. The fact that even this small program will default to second and third data points when the genre preference wasn't good enough is a cool glimpse into, what I assume, a waterfall like structure of it all.

The use of AI in this project was a bit easier to wrangle, one problem I kept having is that it kept wanting to run tests automatically after writing user profiles or re-writing the entire main.py page how it wanted to. But being able to hash out a basic recommendation logic with AI improved the overall quality of MusicBox definitely.
