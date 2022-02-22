# cvat_cli
CVAT command line interface

#### create multiple tasks  
required directory structure  
your_directory_path/task_1_images  
your_directory_path/task_2_images  
your_directory_path/task_3_images  
                   .  
                   .  
```
python worker.py -c your_directory_path  
```
#### delete multiple tasks  
```
python worker.py -r start_task_id end_task_id  
```
#### dump multiple annotations COCO format  
```
python worker.py -d start_task_id end_task_id  
```
