def readJSON_line2(linesIn):
  #Function for reading a chunk of json lines
   '''
   Note, this function is nonsensical. A user would never use the approach suggested 
   for reading in a JSON file, 
   its role is to evaluate the MT approach for full line by line processing to both 
   increase speed and reduce memory overhead
   '''
   import json

   linesRtn = []
   for lineIn in linesIn:

       if lineIn.strip() != 0:
           lineRtn = json.loads(lineIn)
       else:
           lineRtn = ""
        
       linesRtn.append(lineRtn)

   return linesRtn




# -------------------------------------------------------------------
if __name__ == "__main__":
   import multiprocessing as mp

   path1 = "C:\\user\\Documents\\"
   file1 = "someBigJson.json"

   nBuffer = 20*nCPUs  # How many chunks are queued up (so cpus aren't waiting on processes spawning)
   nChunk = 1000 # How many lines are in each chunk
   #Both of the above will require balancing speed against memory overhead

   iJob = 0  #Tracker for SMP jobs submitted into pool
   iiJob = 0  #Tracker for SMP jobs extracted back out of pool

   jobs = []  #SMP job holder
   MTres3 = []  #Final result holder
   chunk = []  
   iBuffer = 0 # Buffer line count
   with open(path1+file1) as f:
      for line in f:
            
          #Send to the chunk
          if len(chunk) < nChunk:
              chunk.append(line)
          else:
              #Chunk full
              #Don't forget to add the current line to chunk
              chunk.append(line)
                
              #Then add the chunk to the buffer (submit to SMP pool)                  
              jobs.append(pool.apply_async(readJSON_line2, args=(chunk,)))
              iJob +=1
              iBuffer +=1
              #Clear the chunk for the next batch of entries
              chunk = []
                            
          #Buffer is full, any more chunks submitted would cause undue memory overhead
          #(Partially) empty the buffer
          if iBuffer >= nBuffer:
              temp1 = jobs[iiJob].get()
              for rtnLine1 in temp1:
                  MTres3.append(rtnLine1)
              iBuffer -=1
              iiJob+=1
            
      #Submit the last chunk if it exists (as it would not have been submitted to SMP buffer)
      if chunk:
          jobs.append(pool.apply_async(readJSON_line2, args=(chunk,)))
          iJob +=1
          iBuffer +=1

      #And gather up the last of the buffer, including the final chunk
      while iiJob < iJob:
          temp1 = jobs[iiJob].get()
          for rtnLine1 in temp1:
              MTres3.append(rtnLine1)
          iiJob+=1

   #Cleanup
   del chunk, jobs, temp1
   pool.close()
