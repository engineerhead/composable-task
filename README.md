The repo contains source code for the given tech task.

Clone the repo and change directory to downloaded one.

    git clone https://github.com/engineerhead/composable-task.git
    cd composable-task
To test  interpreter with provided Bytecode simply run

    python3 interpreter.py

To test with your own byte code, provide the file path of byte code as last argument

    python3 interpreter.py '/path/to/file'

To test the functions that prints put lines in the files matching the given extension, 

    python3 file_lines.py '/path/to/dir' '.ext'
where 3rd and 4th argument are path to directory and extension respectively.

As far as questions in task# 3 are concerned,  as per my understanding the concurrency model mentioned closely resembles Hoare's CSP i.e Communicating sequential processes.

Blocking nature of SEND_CHANNEL and RECIEVE_CHANNEL will likely be accomplished using an infinite loop which keeps sleeping and waking up to see if there is value to send or receive.

Regarding spawning concurrent functions, the following have to be executed after first function is launched

 - Interrupt the first function
 -  Save the stack state 
 - Launch the second function

After few instructions have been executed by 2nd function

 - Save the stack
 - Interrupt the execution
 - Restore the old stack
 - Continue with old function's execution
