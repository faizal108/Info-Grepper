
(function () {

    var resources = [
        {
            id : 0,
            path: "../images/bg-2.jpeg",
            name: 'footer',
            tags: ['html', 'css', 'js'],
            desc: "this is a description of faizal a footer card so ypuo can understand easily",
            likes: 200,
            shares: 300,
            downloads : 500,
            comments : 60
        },
        {
            id : 1,
            path: "../images/bg-3.jfif",
            name: 'header',
            tags: ['html', 'css', 'js','react','php'],
            desc: "this is a description of a card so ypuo can understand easily",
            likes: 400,
            shares: 600,
            downloads : 100,
            comments : 100
        },
        {
            id : 2,
            path: "../images/bg-2.jpeg",
            name: 'Dynamic Footer',
            tags: ['html', 'css', 'sass', 'ruby','angular'],
            desc: "this is a description of a footer card so ypuo can understand easily",
            likes: 2000,
            shares: 3000,
            downloads : 5000,
            comments : 600
        },
        {
            id : 3,
            path: "../images/bg-3.jfif",
            name: 'Dynamic header',
            tags: ['html', 'css', 'js'],
            desc: "this is a description of a footer card so ypuo can understand easily",
            likes: 200,
            shares: 300,
            downloads : 500,
            comments : 60
        },
        {
            id : 4,
            path: "../images/bg-2.jpeg",
            name: 'cards',
            tags: ['html', 'css', 'js','react','php'],
            desc: "this is a description of a card so ypuo can understand easily",
            likes: 400,
            shares: 600,
            downloads : 100,
            comments : 100
        },
        {
            id : 5,
            path: "../images/bg-3.jfif",
            name: 'animated cards',
            tags: ['html', 'css', 'sass', 'ruby','angular'],
            desc: "this is a description of a footer card so ypuo can understand easily",
            likes: 2000,
            shares: 3000,
            downloads : 5000,
            comments : 600
        },
        {
            id : 6,
            path: "../images/bg-2.jpeg",
            name: 'cards',
            tags: ['html', 'css', 'js','react','php'],
            desc: "this is a description of a card so ypuo can understand easily",
            likes: 400,
            shares: 600,
            downloads : 100,
            comments : 100
        },
        {
            id : 78,
            path: "../images/bg-3.jfif",
            name: 'animated cards',
            tags: ['html', 'css', 'sass', 'ruby','angular'],
            desc: "this is a description of a footer card so ypuo can understand easily",
            likes: 2000,
            shares: 3000,
            downloads : 5000,
            comments : 600
        },
        {
            id :8,
            path: "../images/bg-2.jpeg",
            name: 'cards',
            tags: ['html', 'css', 'js','react','php'],
            desc: "this is a description of a card so ypuo can understand easily",
            likes: 400,
            shares: 600,
            downloads : 100,
            comments : 100
        },
        {
            id : 9,
            path: "../images/bg-3.jfif",
            name: 'animated cards',
            tags: ['html', 'css', 'sass', 'ruby','angular'],
            desc: "this is a description of a footer card so ypuo can understand easily",
            likes: 2000,
            shares: 3000,
            downloads : 5000,
            comments : 600
        },
        {
            id : 10,
            path: "../images/bg-2.jpeg",
            name: 'cards',
            tags: ['html', 'css', 'js','react','php'],
            desc: "this is a description of a card so ypuo can understand easily",
            likes: 400,
            shares: 600,
            downloads : 100,
            comments : 100
        },
        {
            id : 11,
            path: "../images/bg-3.jfif",
            name: 'animated cards',
            tags: ['html', 'css', 'sass', 'ruby','angular'],
            desc: "this is a description of a footer card so ypuo can understand easily",
            likes: 2000,
            shares: 3000,
            downloads : 5000,
            comments : 600
        },
        {
            id : 12,
            path: "../images/bg-2.jpeg",
            name: 'cards',
            tags: ['html', 'css', 'js','react','php'],
            desc: "this is a description of a card so ypuo can understand easily",
            likes: 400,
            shares: 600,
            downloads : 100,
            comments : 100
        }
        ];
    var recent_follow = [
        {
            user_name : "@coffee_time",
            user_id : 1
        },
        {
            user_name : "@lets_create",
            user_id : 2
        },
        {
            user_name : "@devthings",
            user_id : 3
        },
        {
            user_name : "@beast_design",
            user_id : 4
        },
        {
            user_name : "@holahola",
            user_id : 5
        },
        {
            user_name : "@moinuddin",
            user_id : 6
        },
        {
            user_name : "@its_me_moin",
            user_id : 7
        },
        {
            user_name : "@coffee_time",
            user_id : 8
        },
        {
            user_name : "@lets_create",
            user_id : 9
        },
        {
            user_name : "@devthings",
            user_id : 10
        },
        {
            user_name : "@beast_design",
            user_id : 11
        },
        {
            user_name : "@holahola",
            user_id : 12
        },
        {
            user_name : "@moinuddin",
            user_id : 13
        },
        {
            user_name : "@its_me_moin",
            user_id : 14
        }

    ];

    angular.module('dashboard', [])
        .controller('searchitems', searchitems)
        .controller('viewController', viewController);
    searchitems.$inject = ['$scope'];
    viewController.$inject = ['$scope'];

    function searchitems($scope) {
        $scope.templetes = resources;
        $scope.recent_follow = recent_follow;
    };

    function viewController($scope) {
        $scope.item = resources;
    };
})();
