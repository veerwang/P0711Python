import asyncio

async def run_python_script(script_path, *args, timeout=None):
    # Create the command to run the Python script
    command = ['python3', script_path] + list(args)
    
    # Create a subprocess and run the command asynchronously
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    try:
        # Wait for the process to complete and capture the output
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)
        
        # Check if the process completed successfully
        if process.returncode == 0:
            return stdout.decode().strip()  # Return the stdout as a string
        else:
            raise Exception(f"Script failed with error: {stderr.decode().strip()}")
    
    except asyncio.TimeoutError:
        # If the process times out, terminate it and raise an exception
        process.terminate()
        await process.wait()  # Ensure the process is cleaned up
        raise Exception(f"Script timed out after {timeout} seconds")

async def main():
    # Path to the Python script you want to run
    script_path = 'A481.py'
    
    # Arguments to pass to the script (if any)
    script_args = ['arg1', 'arg2']
    
    # Set a timeout (in seconds)
    timeout = 5  # 5 seconds timeout
    
    try:
        # Call the script asynchronously and wait for the result
        result = await run_python_script(script_path, *script_args, timeout=timeout)
        print(f"Script output: {result}")
    except Exception as e:
        print(f"Error: {e}")

# Run the main function
asyncio.run(main())
