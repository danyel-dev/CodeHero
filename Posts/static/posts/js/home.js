const btnSortPosts = document.getElementById('btn-sort-posts')

btnSortPosts.addEventListener('click', function() {
    const listSortPosts = document.getElementById('list-sort-posts')
    listSortPosts.classList.toggle('show-block')
})
