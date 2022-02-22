# cvat_cli
CVAT command line interface

create multiple tasks 
python worker.py -c your/directory/path  

delete multiple tasks 
python worker.py -r start_task_id end_task_id  

dump multiple annotations COCO format
python worker.py -d start_task_id end_task_id  
