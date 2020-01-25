const MONTH_NAMES = [
  'Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'İyun',
  'İyul', 'Avqust', 'Sentyabr', 'Oktyabr', 'Noyabr', 'Dekabr'
];


function getFormattedDate(date, prefomattedDate = false, hideYear = false) {
  const day = date.getDate();
  const month = MONTH_NAMES[date.getMonth()];
  const year = date.getFullYear();
  const hours = date.getHours();
  let minutes = date.getMinutes();

  if (minutes < 10) {
    minutes = `0${ minutes }`;
  }

  if (prefomattedDate) {
    return `${ prefomattedDate } saat ${ hours }:${ minutes }`;
  }

  if (hideYear) {
    return `${ day }. ${ month } saat ${ hours }:${ minutes }`;
  }
  return `${ day }. ${ month } ${ year }. saat ${ hours }:${ minutes }`;
}

function timeAgo(dateParam) {
  if (!dateParam) {
    return null;
  }

  const date = typeof dateParam === 'object' ? dateParam : new Date(dateParam);
  const DAY_IN_MS = 86400000; // 24 * 60 * 60 * 1000
  const today = new Date();
  const yesterday = new Date(today - DAY_IN_MS);
  const seconds = Math.round((today - date) / 1000);
  const minutes = Math.round(seconds / 60);
  const isToday = today.toDateString() === date.toDateString();
  const isYesterday = yesterday.toDateString() === date.toDateString();
  const isThisYear = today.getFullYear() === date.getFullYear();


  if (seconds < 5) {
    return 'now';
  } else if (seconds < 60) {
    return `${ seconds } saniyə əvvəl`;
  } else if (seconds < 90) {
    return '1 dəq ərzində';
  } else if (minutes < 60) {
    return `${ minutes } dəqiqə əvvəl`;
  } else if (isToday) {
    return getFormattedDate(date, 'Bugün');
  } else if (isYesterday) {
    return getFormattedDate(date, 'Dünən');
  } else if (isThisYear) {
    return getFormattedDate(date, false, true);
  }

  return getFormattedDate(date);
}
