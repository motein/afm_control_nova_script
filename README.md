# AFM communicates with NOVA
0. Do experiment prepation for both AFM and NOVA
1. AFM calculates a position matrix and then reaches the 1st position.
2. Do Approach and settle some time (wait for servo to be stable).
3. Send a signal to trigger NOVA to do an electrochemical experiment. Meanwhile, AFM will hold the current position.
4. NOVA will create a file named as 'state_fin' to represent Finish state.
5. AFM will use a polling way to check if 'state_fin' exists. Each check will sleep about 0.5 second.
6. If 'state_fin' exists, delete it.
7. Do Withdraw and move AFM tip to the next position.
8. Repeat the 2nd step until all positions have been operated.
