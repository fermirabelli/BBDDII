
SELECT  [EMPLOYEE_ID]
      ,'' as IDENTIFIER
      ,[FIRST_NAME]
      ,[LAST_NAME]
      ,[HIRE_DATE]
      ,[JOB_ID]
      ,[SALARY]
      ,[MANAGER_ID]
      ,[DEPARTMENT_ID] 
	  into  MY_EMPLOYEE
  FROM [EMPLOYEES] where job_id in ('ST_CLERK','IT_PROG')