'''Example 1:'''
try:
    pass
except ValueError:
    pass
except IndexError:
    pass
except NameError:
    pass
except:
    pass

'''Example 2:'''
try:
    pass
except (ValueError, IndexError, NameError):
    pass
except Exception as e:
    pass
else:
    pass
finally:
    pass
