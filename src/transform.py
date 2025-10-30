def transform_universities(data):
    transformed = []
    for uni in data:
        transformed.append({
            "name": uni.get("name"),
            "country": uni.get("country"),
            "domains": uni.get("domains"),
            "web_pages": uni.get("web_pages")
        })
    return transformed
