
(function () {
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
