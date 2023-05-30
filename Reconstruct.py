def reconstruct_tree(inorder_sequence, postorder_sequence):
    if not postorder_sequence:
        return None

    main_node = postorder_sequence[-1]
    if isinstance(main_node,str):
        node = [[','.join(str(x) for x in main_node)], None, None]
    else:
        node = [main_node, None, None]
   

    node_index = inorder_sequence.index(main_node)
    left_inorder = inorder_sequence[:node_index]
    right_inorder = inorder_sequence[node_index+1:]

    left_postorder = postorder_sequence[:len(left_inorder)]
    right_postorder = postorder_sequence[len(left_inorder):-1]

    node[1] = reconstruct_tree(left_inorder, left_postorder)
    node[2] = reconstruct_tree(right_inorder, right_postorder)

    return node


inorder_seq = ["h", "i", "t", "e", "a", "m", 130]
postorder_seq = ["h", "i", "e", "a", 130, "m", "t"]
print(reconstruct_tree(inorder_seq, postorder_seq))