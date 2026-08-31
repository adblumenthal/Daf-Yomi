# Acceptance cases

Use these as manual/agent acceptance tests before publishing a release.

## Core date behavior

1. `/dafyomi`
   - Uses the user's current local date.
   - States Gregorian and Hebrew date.
   - Gives today's correct Daf Yomi assignment.

2. `/dafyomi yesterday`
   - Uses the user's local yesterday, not UTC yesterday.

3. `/dafyomi 8/15/2025`
   - Interprets as August 15, 2025 (U.S. month/day/year).

4. `/dafyomi 2025-08-15`
   - Resolves the same date unambiguously.

## Catch-up

5. `/dafyomi 8/15/2025 till today short`
   - Covers every assigned daf in the range.
   - Groups intelligently rather than outputting full daily lessons.
   - Includes a compact checklist of dafim covered.

6. Catch-up range crossing a masechet boundary
   - Calls out the siyum/transition clearly.

## Siyum planning

7. A daf 15+ days from the end of its masechet
   - Gives days remaining, but no exact-date siyum planning banner is required.

8. A daf 14 days from the end
   - Gives the exact Gregorian completion date and Hebrew date when available.

9. A daf 7 days from the end
   - Makes the siyum reminder more prominent.

10. A daf 3 days from the end
    - Explicitly tells the learner this is the time to make siyum plans.

11. Final daf of a masechet
    - Reports `0 days — siyum day`.
    - Celebrates succinctly.
    - Names tomorrow's next masechet when reliably known.

## Special days

12. Daf Yomi on Yom Kippur.
13. Daf Yomi on Tisha B'Av.
14. Daf Yomi on Rosh Chodesh.
    - Each should mention the calendar context succinctly without overwhelming the lesson.

## Learning modes

15. `/dafyomi beginner`
    - Explains terminology and logical flow more slowly.
    - Adds useful pronunciation/transliteration.

16. `/dafyomi advanced deep`
    - Reduces elementary definitions.
    - Emphasizes Rishonim, conceptual distinctions, and exact references where useful.

17. `/dafyomi halacha beginner`
    - Keeps practical halacha prominent while remaining accessible.

18. `/dafyomi short`
    - Produces a genuinely compact lesson with key points, limited commentary, Aramaic, and review.

## Source behavior

19. `/dafyomi show sources`
    - Gives direct Sefaria links to the Gemara and relevant commentary actually discussed.
    - Distinguishes consulted sources from related resources.

20. Simulate Hebcal unavailable
    - Does not invent a Daf Yomi assignment.
    - Clearly distinguishes verified vs. not live-verified information.

21. Simulate Sefaria unavailable
    - Does not fabricate Rashi/Tosafot or quotations.
    - Continues only with material that can be stated reliably.

## Teaching quality

22. A daf with a complicated shakla v'tarya
    - Uses a compact question → proof → rejection → conclusion map when it improves clarity.

23. A daf with an abstract conceptual dispute
    - Explains why the Gemara cares.

24. A daf featuring a major Tanna/Amora
    - Gives a one-phrase identification only when useful.

25. Default lesson
    - Starts with perek/continuity context when reliably known.
    - Contains exactly three concise key takeaways.
    - Ends with a one-sentence tomorrow preview when reliably determinable.
