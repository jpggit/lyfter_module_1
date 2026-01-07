#1. Crea un `bubble_sort` por tu cuenta sin revisar el código de la lección.

def bubble_sort(list): 
    for outer_index in range (0, len(list)-1): 
        has_made_changes = False 

        for index in range (0, len(list)-1-outer_index): 
            current_item = list[index] 
            next_item = list[index+1]

            if current_item > next_item:
                list[index] = next_item
                list[index+1] = current_item
                has_made_changes = True
        
        if not has_made_changes:
            return