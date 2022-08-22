# cvat_cli
CVAT command line interface

You have to edit auth, host, port in worker.py

### create multiple tasks  
#### required directory structure  
images_directory/task_1_images  
images_directory/task_2_images  
images_directory/task_3_images  
                   .  
                   .  
```
python worker.py -c images_directory --labels label_file_path
```
### delete multiple tasks  
```
python worker.py -r start_task_id end_task_id  
```
### dump multiple annotations COCO format  
```
python worker.py -d start_task_id end_task_id  
```
