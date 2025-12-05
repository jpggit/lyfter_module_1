#1. Crea un `bubble_sort` por tu cuenta sin revisar el código de la lección.
#2. Modifica el `bubble_sort` para que funcione de derecha a izquierda, 
# ordenando los números menores primero (como en la imagen de abajo).

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
        

def bubble_sort_right_to_left(list):
    for outer_index in range (0, len(list)-1):
        has_made_changes = False

        for index in range(len(list) - 1, outer_index, -1):
            current_item = list[index]
            next_item = list[index-1]

            if current_item < next_item:
                list[index] = next_item
                list[index+-1] = current_item
                has_made_changes = True
        
        if not has_made_changes:
            return