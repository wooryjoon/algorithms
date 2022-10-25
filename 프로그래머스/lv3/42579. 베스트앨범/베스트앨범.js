function solution(genres, plays) {
    
    var answer = [];
    const songs = [];
    const genreSumHash = {};
    const genreSumArr = [];
    genres.forEach((genre,idx) => {
        songs.push({id : idx, genre : genre, play : plays[idx]})
    genreSumHash[genre] === undefined ? genreSumHash[genre] = plays[idx] : genreSumHash[genre] += plays[idx];
    })
    
    for (let key in genreSumHash) {
        genreSumArr.push([key,genreSumHash[key]]);
    }
    genreSumArr.sort((a,b) => b[1] - a[1]);
    // 내림차순 정렬 완료
    for (let k of genreSumArr) {
        let sorted = songs.filter((user) => user.genre === k[0]);        
        sorted.sort((a,b) => b.play - a.play);
        for (let i = 0; i < 2 && i < sorted.length; i++) {
            answer.push(sorted[i].id);
        }

    }
    return answer;
}