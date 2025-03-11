class Book {
    constructor(title, author, year, genre) {
        this.title = title;
        this.author = author;
        this.year = year;
        this.genre = genre;
    }

    getInfo() {
        return `${this.title} by ${this.author}, published in ${this.year}`;
    }

    changeTitle(newTitle) {
        this.title = newTitle;
    }

    changeAuthor(newAuthor) {
        this.author = newAuthor;
    }

}


class EBook extends Book {
    constructor(title, author, year, genre, fileSize) {
        super(title, author, year, genre);
        this.fileSize = fileSize;
    }

    getFileSize() {
        return this.fileSize;
    }
}

class AudioBook extends Book {
    constructor(title, author, year, genre, duration) {
        super(title, author, year, genre);
        this.duration = duration;
    }

    getDuration() {
        return this.duration;
    }
}
