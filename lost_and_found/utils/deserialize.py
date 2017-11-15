def deserialize(serializer_class, data, **kwargs):
    if serializer_class and data is not None:
        serializer = serializer_class(data=data, **kwargs)
        if serializer.is_valid(raise_exception=True):
            input_type_obj = serializer.save()
            return input_type_obj
        else:
            raise SyntaxError(str(serializer.errors))
    return None
