def get_process_privileges(pid):
try:
  # obtain a handle to the target process
  hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_¬
  INFORMATION,False,pid)
  # open the main process token
  htok = win32security.OpenProcessToken(hproc,win32con.TOKEN_QUERY)
  # retrieve the list of privileges enabled
  privs = win32security.GetTokenInformation(htok, win32security.¬
  TokenPrivileges)
  
  # iterate over privileges and output the ones that are enabled
  priv_list = ""
  for i in privs:
    # check if the privilege is enabled
    if i[1] == 3:
      priv_list += "%s|" % win32security.¬
      LookupPrivilegeName(None,i[0])
except:
  priv_list = "N/A"
return 
  priv_list
