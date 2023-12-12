def get_label_vars(labels):
    if type(labels[0]) is not bool:
        return [label_var.get() for label_var in labels]
    else:
        return labels


def check_condition(faze_state_buffer, navi_state_buffer):
    return get_label_vars(faze_state_buffer), get_label_vars(navi_state_buffer)
