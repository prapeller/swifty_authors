class ArticleReadTimeEngine:

    def __init__(self, article):
        self.article = article
        self.words_per_minute = 250
        self.banner_image_adjustment_time = round(1 / 6, 3)

    def check_article_has_banner_image(self):
        has_banner_image = True
        if not self.article.banner_image:
            has_banner_image = False
            self.banner_image_adjustment_time = 0
        return has_banner_image

    def get_title(self):
        return self.article.title

    def get_tags(self):
        tags = []
        [tags.extend(tag.split()) for tag in self.article.list_of_tags]
        return tags

    def get_body(self):
        return self.article.body

    def get_description(self):
        return self.article.description

    def get_article_details(self):
        details = []
        details.extend(self.get_title().split())
        details.extend(self.get_body().split())
        details.extend(self.get_description().split())
        details.extend(self.get_tags())
        return details

    def get_read_time(self):
        article_length = len(self.get_article_details())
        self.check_article_has_banner_image()

        if article_length:
            read_time_in_minutes = article_length / self.words_per_minute
            banner_time_in_minutes = self.banner_image_adjustment_time / 60
            if read_time_in_minutes > 1:
                return f"{read_time_in_minutes + banner_time_in_minutes} minutes"
            else:
                return f"{(read_time_in_minutes + banner_time_in_minutes) * 60} seconds"