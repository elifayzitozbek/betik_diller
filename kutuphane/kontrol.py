# kutuphane/kontrol.py
class SchemaError(Exception):
    pass

def zorunlu_alanlar(gerekenler):
    def decorator(func):
        def wrapper(df, *args, **kwargs):
            eksikler = [k for k in gerekenler if k not in df.columns]
            if eksikler:
                raise SchemaError(f"Eksik kolon(lar): {', '.join(eksikler)}")
            return func(df, *args, **kwargs)
        return wrapper
    return decorator
