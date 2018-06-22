# AFM commnucates with NOVA
1. AFM calculates a position matrix and then reaches the 1st position.
2. Do Approach and settle some time.
3. Send a signal to trigger NOVA to do an electrochemical experiment.
4. NOVA will create a file named as 'state_fin' to represent Finish state.
5. AFM will use a polling way to check if 'state_fin' exists. Each check will sleep 0.5 second.
6. If 'state_fin' exists, delete it and move AFM tip to the next position.
7. Repeat the 2nd step until all positions have been operated.
