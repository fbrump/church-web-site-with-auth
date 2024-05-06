const getSmallGroups = () => {
    const items = [
        {
            id: 'c4b962de-2342-4e63-9e93-03ca03dd9f8a',
            title: 'Men',
            weekday: 'Monday',
            startAt: 20,
            finishAt: 21
        },
        {
            id: '11dd0de8-3564-4369-96db-1f07a8de2d17',
            title: 'Women',
            weekday: 'Thursday',
            startAt: 20,
            finishAt: 21
        },
        {
            id: 'c5fb92c1-cf24-4aac-91f4-ebfe5e382aa0',
            title: 'Kids',
            weekday: 'Saturday',
            startAt: 15,
            finishAt: 16
        }
    ];
    
    return items.sort(t => t.title);
}

const getSmallGroup = (id) => {
    console.log(id);
    const items = getSmallGroups();
    
    const filtered = items.filter(item => item.id === id);
    console.log('Filter');
    console.log(filtered)
    return filtered.length === 1 ? filtered[0] : null;
}

export { getSmallGroups, getSmallGroup };